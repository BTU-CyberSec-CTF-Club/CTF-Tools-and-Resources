#!/bin/bash
FILE=$1

header() {
    text=$1
    TEXT=$(echo "$text" | tr '[:lower:]' '[:upper:]')
    echo
    echo "## $TEXT ##"
}

## VALIDATION
if ! command -v tshark &>/dev/null; then
    echo "ERROR: tshark is not installed. Please install Wireshark/tshark first."
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: $0 <pcap file>"
    exit 1
fi

FILE="$1"
if [ ! -f "$FILE" ]; then
    echo "ERROR: File '$FILE' not found."
    exit 1
fi

## EXECUTION
header "General PCAP Infos"
capinfos "$FILE"

header "IP Endpoints"
tshark -r "$FILE" -q -z endpoints,ip

header "Ethernet Endpoints"
tshark -r "$FILE" -q -z endpoints,eth

header "IP Conversations"
tshark -r "$FILE" -q -z conv,ip

header "Protocol Overview"
tshark -r "$FILE" -q -z io,phs

header "TCP Streams Overview"
tshark -r "$FILE" -T fields -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport |
    awk 'BEGIN {FS="\t"; OFS="\t"}
$1 ~ /^[0-9]+$/ && $2!="" && $3!="" && $4!="" && $5!="" {
    key = $1
    if (!seen[key]++) {
        a = $2":"$3; b = $4":"$5
        if (a < b) print key, a, "<->", b
        else       print key, b, "<->", a
    }
}' | (
    echo -e "Stream\tSource\t\tDest"
    cat
) | column -t -s $'\t'

header "HTTP Requests Overview"
# (
# echo -e "Method\tStatus\tURI\tSrc_IP\tDst_IP"
# tshark -r "$FILE" -Y "http" -T fields -e http.request.method -e http.response.code -e http.request.uri -e ip.src -e ip.dst | sort -u
# ) | column -t -s $'\t'
tshark -r "$FILE" -Y "http" \
    -T fields \
    -e frame.number \
    -e tcp.stream \
    -e ip.src \
    -e ip.dst \
    -e http.request.method \
    -e http.request.uri \
    -e http.response.code |
    sort -t$'\t' -k1 -n |
    awk '
BEGIN { FS="\t"; OFS="\t" }
{
  frame=$1; stream=$2; src=$3; dst=$4; method=$5; uri=$6; status=$7

  if (method != "") {
    req_frame[frame] = frame
    req_stream[frame] = stream
    req_method[frame] = method
    req_uri[frame]    = uri
    req_src[frame]    = src
    req_dst[frame]    = dst
    queue[stream, ++cnt[stream]] = frame
  }

  if (status != "") {
    for (i = 1; i <= cnt[stream]; i++) {
      req = queue[stream, i]
      if (!(req in paired)) {
        resp_status[req] = status
        paired[req] = 1
        break
      }
    }
  }
}
END {
  n = asorti(req_frame, sorted_frames)
  for (i = 1; i <= n; i++) {
    f = sorted_frames[i]
    method = req_method[f]
    uri    = req_uri[f]
    src    = req_src[f]
    dst    = req_dst[f]
    st     = (f in resp_status) ? resp_status[f] : "???"
    stream = req_stream[f]
    print method, st, uri, src, dst, stream
  }
}' |
    awk '
BEGIN { FS="\t"; OFS="\t" }
{
  method=$1; status=$2; uri=$3; client=$4; server=$5; stream=$6
  key = method OFS status OFS uri OFS client OFS server
  if (!(key in seen)) {
    order[++n] = key
    seen[key] = 1
  }
  stream_count[key, stream]++
  if (!((key, stream) in stream_added)) {
    stream_added[key, stream] = 1
    if (stream_list[key] == "")
      stream_list[key] = stream
    else
      stream_list[key] = stream_list[key] "," stream
  }
}
END {
  print "Method", "Status", "URI", "Client_IP", "Server_IP", "Streams"
  for (i = 1; i <= n; i++) {
    key = order[i]
    split(key, arr, OFS)
    method=arr[1]; status=arr[2]; uri=arr[3]; client=arr[4]; server=arr[5]
    split(stream_list[key], streams_arr, ",")
    stream_out = ""
    for (j = 1; j <= length(streams_arr); j++) {
      s = streams_arr[j]
      cnt = stream_count[key, s]
      if (j > 1) stream_out = stream_out ","
      if (cnt > 1) stream_out = stream_out s " (" cnt "x)"
      else stream_out = stream_out s
    }
    print method, status, uri, client, server, stream_out
  }
}' | column -t -s $'\t'

header "Hints / Next Steps"
echo "* View a full TCP stream: tshark -r '$FILE' -q -z follow,tcp,ascii,<stream_number>"
echo "* Export HTTP objects: tshark -r '$FILE' --export-objects http,<dir>"
echo "* Extract specific packets: tshark -r '$FILE' -Y '<filter>' -w subset.pcap"

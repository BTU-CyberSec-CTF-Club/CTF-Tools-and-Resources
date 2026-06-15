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
tshark -r "$FILE" -T fields -e ip.src -e ip.dst | sort -u

header "Ethernet Endpoints"
tshark -r "$FILE" -q -z endpoints,eth

header "IP Conversations"
tshark -r "$FILE" -q -z conv,ip

header "Protocol Overview"
tshark -r "$FILE" -q -z io,phs

header "TCP Streams Overview"
tshark -r "$FILE" -T fields -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport | awk '
$1 ~ /^[0-9]+$/ && $2 != "" && $3 != "" && $4 != "" && $5 != "" {
    a = $2":"$3
    b = $4":"$5
    key = $1
    if (a < b) pair = a " <-> " b; else pair = b " <-> " a
    if (!seen[key]++) print key "\t" pair
}'

header "HTTP Requests Overview"
tshark -r shark1.pcapng -Y "http" -T fields -e http.request.method -e http.request.uri -e http.response.code | sort -u
tshark -r "$FILE" -q -z io,phs

header "Hints / Next Steps"
echo "* View a full TCP stream: tshark -r <file> -q -z follow,tcp,ascii,<stream_number>"
echo "* Export HTTP objects: tshark -r <file> --export-objects http,<dir>"
echo "* Extract specific packets: tshark -r <file> -Y '<filter>' -w subset.pcap"

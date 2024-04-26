#!/bin/bash
# This script sends a GET request with a custom header and displays the body of the response.
curl -s "$1" -H "X-School-User-Id: 98"

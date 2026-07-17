Analyze /app/access.log and save the results to /app/report.json.

The report must be valid JSON with this exact structure:

{
  "total_requests": <integer>,
  "clients": {
    "<client IP>": <request count>
  },
  "popular_pages": {
    "<page path>": <request count>
  }
}
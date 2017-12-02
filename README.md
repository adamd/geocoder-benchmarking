# geocoder-benchmarking
Little Python script to benchmark geocoders or any series of URLs using [grequests](https://github.com/kennethreitz/grequests).

## Usage

`python benchmarks.py example.txt 5`

Loops through example.txt file containing a list of URLs. Sends 5 requests at a time, waiting for all to return, and timing them as a batch.

## Output

```
Total seconds:	2.061178
Total requests:	10
Successful req:	10
```

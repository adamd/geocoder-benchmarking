import grequests
from datetime import datetime
import sys
import os.path
from time import sleep
from hashlib import sha1
import hmac

def test_batch(urls):
  rs = (grequests.get(u) for u in urls)
  stamp_start = datetime.now()
  responses = grequests.map(rs)
  stamp_end = datetime.now()
  stamp_diff = stamp_end - stamp_start

  return {"timing": stamp_diff, "responses": responses}

def prep_tests(fn, batch_size):
    # Set benchmark variables
    total_seconds = 0
    total_requests = 0
    successful_requests = 0
    # Loop through file "fn"
    remaining = os.path.getsize(fn)
    with open(fn, 'r') as fh:
        batch = []
        for line in fh:
            batch.append(line)
            remaining -= len(line)
            if (len(batch) == batch_size or remaining == 0):
                result = test_batch(batch)
                batch = []
                total_seconds += result["timing"].total_seconds()
                for r in result["responses"]:
                    total_requests += 1
                    if r.status_code != None:
                        if r.status_code == 200:
                            successful_requests += 1
                            #print r.url
                        else:
                            print str(r.status_code)
                            print r.headers
    fh.close()
    # Report on tests
    print "Total seconds:\t" + str(total_seconds)
    print "Total requests:\t" + str(total_requests)
    print "Successful req:\t" + str(successful_requests)

def main():
    # Grab args
    if (len(sys.argv) == 1):
        print "Requires filename argument"
    else:
        fn = sys.argv[1]
        atatime = 10
        if (len(sys.argv) > 2):
            atatime = int(sys.argv[2])
        # Check file exists
        if (os.path.exists(fn)):
            prep_tests(fn, atatime)
        else:
            print "File not found"

if __name__ == "__main__":
  main()

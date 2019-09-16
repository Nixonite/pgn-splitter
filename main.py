import os, uuid

def chunks(l, n):
  """Yield successive n-sized chunks from l."""
  for i in range(0, len(l), n):
    yield l[i:i + n]

if __name__ == "__main__":
  split_by_count = 5000 # num games
  games = list(filter(lambda x: x.endswith('.pgn'), os.listdir()))
  for filename in games:
    data = open(filename, encoding='ISO-8859-1').read()
    zipped_pgns = zip(data.split('\n\n')[::2], data.split('\n\n')[1::2])
    split_pgns_list = list(map(lambda x: x[0] + '\n\n' + x[1], zipped_pgns))
    
    chunked_pgns = chunks(split_pgns_list, split_by_count)
    for chunk in chunked_pgns:
      with open(uuid.uuid4().hex + '.pgn', 'w') as f:
        f.write('\n\n'.join(chunk))
        f.close()
    os.remove(filename)
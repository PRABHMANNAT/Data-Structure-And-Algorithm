import base64
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from workbench.native import execute
from workbench.validation import text

def run(data):
    content=text(data,'text').encode('utf-8')
    with TemporaryDirectory(prefix='dsa-huffman-') as directory:
        source=Path(directory)/'input.txt';archive=Path(directory)/'output.huf';decoded=Path(directory)/'decoded.txt'
        source.write_bytes(content)
        execute('file-zipper-huffman','\n'.join(map(str,[source,archive,decoded])),sources=['src/huffman.cpp'])
        packed=archive.read_bytes();restored=decoded.read_bytes()
    return dict(input_bytes=len(content),archive_bytes=len(packed),verified=restored==content,decoded=restored.decode('utf-8'),
                archive=base64.b64encode(packed).decode('ascii'),frequencies=Counter(content).most_common(20))

"""Run real project suites and browser-adapter contracts without pip packages."""
from pathlib import Path
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
TEMP=ROOT/'.workbench-cache/tmp'
TEMP.mkdir(parents=True,exist_ok=True)
tempfile.tempdir=str(TEMP)
os.environ['TMP']=str(TEMP)
os.environ['TEMP']=str(TEMP)
PYTHON_PROJECTS=['intermediate_data_structures','advanced_delivery_network','algorithmic_transit_simulator',
                 'versioned_search_engine','plagiarism_detection_system','string_algorithms_lab','graphforge','streamshield']


def command(args,cwd=ROOT,timeout=180):
    print('\n$ '+' '.join(map(str,args)),flush=True)
    environment=os.environ.copy()
    environment['PYTHONPATH']=os.pathsep.join([str(ROOT),str(cwd)])
    try:
        return subprocess.run(list(map(str,args)),cwd=cwd,timeout=timeout,env=environment).returncode==0
    except (OSError,subprocess.TimeoutExpired) as error:
        print(f'Could not execute verification: {error}',flush=True)
        return False


def web_tests():
    suite=unittest.defaultTestLoader.discover(str(ROOT/'workbench/tests'))
    for index,path in enumerate(sorted(ROOT.glob('*/web/test_adapter.py'))+sorted(ROOT.glob('Number System/*/web/test_adapter.py'))):
        spec=importlib.util.spec_from_file_location('project_web_test_'+str(index),path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
    return unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--web',action='store_true',help='Only browser adapters and HTTP contracts')
    parser.add_argument('--python',action='store_true',help='Only original Python suites')
    parser.add_argument('--go',action='store_true',help='Only Go suites')
    parser.add_argument('--cpp',action='store_true',help='Only original C++ suites')
    args=parser.parse_args();all_suites=not any(vars(args).values());results=[]
    if args.web or all_suites:results.append(web_tests())
    if args.python or all_suites:
        for folder in PYTHON_PROJECTS:
            suite=['pytest','tests','-q','-p','no:cacheprovider'] if folder in ['graphforge','streamshield'] else ['unittest','discover','-s','tests','-q']
            results.append(command([sys.executable,'-m',*suite],ROOT/folder))
    if args.go or all_suites:
        for manifest in sorted(ROOT.glob('*/go.mod')):
            results.append(command(['go','test','./...'],manifest.parent))
    if args.cpp or all_suites:
        from workbench.native import compiler
        cxx=compiler();cache=ROOT/'.workbench-cache';cache.mkdir(exist_ok=True)
        suites=[('cpp-dsa-toolkit','tests/structures_tests.cpp',[]),('cpp-dsa-toolkit','tests/algorithms_tests.cpp',[]),
                ('splitwise-cashflow-minimizer','tests/cashflow_tests.cpp',['src/balance_calculator.cpp','src/heap_settler.cpp']),
                ('file-zipper-huffman','tests/round_trip.cpp',['src/huffman.cpp'])]
        for index,(folder,test,sources) in enumerate(suites):
            binary=cache/('suite-'+str(index)+('.exe' if os.name=='nt' else ''))
            built=command([cxx,'-std=c++20','-O2','-Iinclude',test,*sources,'-o',binary],ROOT/folder)
            results.append(built and command([binary],TEMP))
    if all_suites:
        results.append(command(['node','tests/puzzle-model.test.mjs'],ROOT/'12-crossword-puzzle-game'))
        results.append(command(['node','--test','tests/search.test.mjs'],ROOT/'11-map-routing-pathfinding-visualizer'))
    print(f'\n{sum(results)}/{len(results)} verification groups passed',flush=True)
    return 0 if results and all(results) else 1


if __name__=='__main__':raise SystemExit(main())

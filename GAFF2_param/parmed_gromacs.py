import parmed as pmd

amber = pmd.load_file('1m.parm7','1m.rst7')
amber.save('1m.top')
amber.save('1m.gro')

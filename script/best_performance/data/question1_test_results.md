# Resultados do Teste - question1.py

```bash
(db-sicred-py3.11) ➜  db-sicred git:(develop) ✗ mprof run script/best_performance/question1.py
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Filename: script/best_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.1 MiB     22.1 MiB           1   @profile
     7                                         def main(range_limit: int) -> None:
     8     22.1 MiB      0.0 MiB        1002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
     9     22.1 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    10     22.1 MiB      0.0 MiB           1       top_n = 3
    11
    12     22.1 MiB      0.0 MiB           1       contracts = Contracts()
    13     22.1 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    14     22.1 MiB      0.0 MiB           1           open_contracts,
    15     22.1 MiB      0.0 MiB           1           renegotiated_contracts,
    16     22.1 MiB      0.0 MiB           1           top_n,
    17                                             )


Time: 0.028753280639648438 for 1000 Contracts
Filename: script/best_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.1 MiB     22.1 MiB           1   @profile
     7                                         def main(range_limit: int) -> None:
     8     22.7 MiB      0.6 MiB        5002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
     9     22.7 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    10     22.7 MiB      0.0 MiB           1       top_n = 3
    11
    12     22.7 MiB      0.0 MiB           1       contracts = Contracts()
    13     22.7 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    14     22.7 MiB      0.0 MiB           1           open_contracts,
    15     22.7 MiB      0.0 MiB           1           renegotiated_contracts,
    16     22.7 MiB      0.0 MiB           1           top_n,
    17                                             )


Time: 0.12148666381835938 for 5000 Contracts
Filename: script/best_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.7 MiB     22.7 MiB           1   @profile
     7                                         def main(range_limit: int) -> None:
     8     23.5 MiB      0.8 MiB       10002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
     9     23.5 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    10     23.5 MiB      0.0 MiB           1       top_n = 3
    11
    12     23.5 MiB      0.0 MiB           1       contracts = Contracts()
    13     23.5 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    14     23.5 MiB      0.0 MiB           1           open_contracts,
    15     23.5 MiB      0.0 MiB           1           renegotiated_contracts,
    16     23.5 MiB      0.0 MiB           1           top_n,
    17                                             )


Time: 0.2369837760925293 for 10000 Contracts
Filename: script/best_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     23.5 MiB     23.5 MiB           1   @profile
     7                                         def main(range_limit: int) -> None:
     8     28.9 MiB      5.4 MiB       50002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
     9     28.9 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    10     28.9 MiB      0.0 MiB           1       top_n = 3
    11
    12     28.9 MiB      0.0 MiB           1       contracts = Contracts()
    13     29.0 MiB      0.1 MiB           2       contracts.get_top_N_open_contracts(
    14     28.9 MiB      0.0 MiB           1           open_contracts,
    15     28.9 MiB      0.0 MiB           1           renegotiated_contracts,
    16     28.9 MiB      0.0 MiB           1           top_n,
    17                                             )


Time: 1.1945443153381348 for 50000 Contracts
Filename: script/best_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     25.6 MiB     25.6 MiB           1   @profile
     7                                         def main(range_limit: int) -> None:
     8     35.1 MiB      9.5 MiB      100002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
     9     35.1 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    10     35.1 MiB      0.0 MiB           1       top_n = 3
    11
    12     35.1 MiB      0.0 MiB           1       contracts = Contracts()
    13     35.8 MiB      0.7 MiB           2       contracts.get_top_N_open_contracts(
    14     35.1 MiB      0.0 MiB           1           open_contracts,
    15     35.1 MiB      0.0 MiB           1           renegotiated_contracts,
    16     35.1 MiB      0.0 MiB           1           top_n,
    17                                             )


Time: 2.3476130962371826 for 100000 Contracts
```

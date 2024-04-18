# Resultados do Teste - question1.py

```bash
(db-sicredi-py3.11) ➜  db-sicredi git:(develop) ✗ mprof run script/worst_performance/question1.py
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Filename: script/worst_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.1 MiB     22.1 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     22.1 MiB      0.0 MiB        1002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    10     22.1 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    11     22.1 MiB      0.0 MiB           1       top_n = 3
    12
    13     22.1 MiB      0.0 MiB           1       contracts = Contracts()
    14     22.1 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    15     22.1 MiB      0.0 MiB           1           open_contracts,
    16     22.1 MiB      0.0 MiB           1           renegotiated_contracts,
    17     22.1 MiB      0.0 MiB           1           top_n,
    18                                             )


Time: 0.34731554985046387 for 1000 Contracts
Filename: script/worst_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.1 MiB     22.1 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     22.8 MiB      0.6 MiB        5002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    10     22.8 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    11     22.8 MiB      0.0 MiB           1       top_n = 3
    12
    13     22.8 MiB      0.0 MiB           1       contracts = Contracts()
    14     22.8 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    15     22.8 MiB      0.0 MiB           1           open_contracts,
    16     22.8 MiB      0.0 MiB           1           renegotiated_contracts,
    17     22.8 MiB      0.0 MiB           1           top_n,
    18                                             )


Time: 8.269911289215088 for 5000 Contracts
Filename: script/worst_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.8 MiB     22.8 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     23.5 MiB      0.8 MiB       10002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    10     23.5 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    11     23.5 MiB      0.0 MiB           1       top_n = 3
    12
    13     23.5 MiB      0.0 MiB           1       contracts = Contracts()
    14     23.5 MiB      0.0 MiB           2       contracts.get_top_N_open_contracts(
    15     23.5 MiB      0.0 MiB           1           open_contracts,
    16     23.5 MiB      0.0 MiB           1           renegotiated_contracts,
    17     23.5 MiB      0.0 MiB           1           top_n,
    18                                             )


Time: 32.73543190956116 for 10000 Contracts
Filename: script/worst_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     23.5 MiB     23.5 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     28.7 MiB      5.2 MiB       50002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    10     28.7 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    11     28.7 MiB      0.0 MiB           1       top_n = 3
    12
    13     28.7 MiB      0.0 MiB           1       contracts = Contracts()
    14     29.7 MiB      1.1 MiB           2       contracts.get_top_N_open_contracts(
    15     28.7 MiB      0.0 MiB           1           open_contracts,
    16     28.7 MiB      0.0 MiB           1           renegotiated_contracts,
    17     28.7 MiB      0.0 MiB           1           top_n,
    18                                             )


Time: 807.0730130672455 for 50000 Contracts
Filename: script/worst_performance/question1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     26.7 MiB     26.7 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     36.2 MiB      9.5 MiB      100002       open_contracts = [Contract(index, index) for index in range(1, range_limit, 1)]
    10     36.2 MiB      0.0 MiB           1       renegotiated_contracts = [3]
    11     36.2 MiB      0.0 MiB           1       top_n = 3
    12
    13     36.2 MiB      0.0 MiB           1       contracts = Contracts()
    14     36.5 MiB      0.3 MiB           2       contracts.get_top_N_open_contracts(
    15     36.2 MiB      0.0 MiB           1           open_contracts,
    16     36.2 MiB      0.0 MiB           1           renegotiated_contracts,
    17     36.2 MiB      0.0 MiB           1           top_n,
    18                                             )


Time: 3220.429465532303 for 100000 Contracts
```

# Resultados do Teste - question2.py

```bash
db-sicred-py3.11➜  db-sicred git:(develop) ✗ mprof run script/worst_performance/question2.py
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Filename: script/worst_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     21.9 MiB      0.0 MiB        1002       requests = [number for number in range(1, range_limit, 1)]
    10     21.9 MiB      0.0 MiB           1       n_max = 3
    11
    12     21.9 MiB      0.0 MiB           1       orders = Orders()
    13     21.9 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 0.34633827209472656 for 1000 Contracts
Filename: script/worst_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     21.9 MiB      0.0 MiB        5002       requests = [number for number in range(1, range_limit, 1)]
    10     21.9 MiB      0.0 MiB           1       n_max = 3
    11
    12     21.9 MiB      0.0 MiB           1       orders = Orders()
    13     21.9 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 7.877495050430298 for 5000 Contracts
Filename: script/worst_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     22.3 MiB      0.4 MiB       10002       requests = [number for number in range(1, range_limit, 1)]
    10     22.3 MiB      0.0 MiB           1       n_max = 3
    11
    12     22.3 MiB      0.0 MiB           1       orders = Orders()
    13     22.3 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 30.828795909881592 for 10000 Contracts
Filename: script/worst_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.3 MiB     22.3 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     23.8 MiB      1.5 MiB       50002       requests = [number for number in range(1, range_limit, 1)]
    10     23.8 MiB      0.0 MiB           1       n_max = 3
    11
    12     23.8 MiB      0.0 MiB           1       orders = Orders()
    13     23.2 MiB     -0.7 MiB           1       orders.combine_orders(requests, n_max)


Time: 779.1668980121613 for 50000 Contracts
Filename: script/worst_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     23.2 MiB     23.2 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     26.2 MiB      3.0 MiB      100002       requests = [number for number in range(1, range_limit, 1)]
    10     26.2 MiB      0.0 MiB           1       n_max = 3
    11
    12     26.2 MiB      0.0 MiB           1       orders = Orders()
    13     23.7 MiB     -2.5 MiB           1       orders.combine_orders(requests, n_max)


Time: 3104.658012866974 for 100000 Contracts
```

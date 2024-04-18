# Resultados do Teste - question2.py

```bash
db-sicredi-py3.11➜  db-sicredi git:(develop) ✗ mprof run script/best_performance/question2.py
mprof: Sampling memory every 0.1s
running new process
running as a Python program...
Filename: script/best_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     21.9 MiB      0.0 MiB        1002       requests = [number for number in range(1, range_limit, 1)]
    10     21.9 MiB      0.0 MiB           1       n_max = 3
    11
    12     21.9 MiB      0.0 MiB           1       orders = Orders()
    13     21.9 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 0.027398347854614258 for 1000 Contracts
Filename: script/best_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     21.9 MiB      0.0 MiB        5002       requests = [number for number in range(1, range_limit, 1)]
    10     21.9 MiB      0.0 MiB           1       n_max = 3
    11
    12     21.9 MiB      0.0 MiB           1       orders = Orders()
    13     21.9 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 0.11780405044555664 for 5000 Contracts
Filename: script/best_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     21.9 MiB     21.9 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     22.3 MiB      0.4 MiB       10002       requests = [number for number in range(1, range_limit, 1)]
    10     22.3 MiB      0.0 MiB           1       n_max = 3
    11
    12     22.3 MiB      0.0 MiB           1       orders = Orders()
    13     22.3 MiB      0.0 MiB           1       orders.combine_orders(requests, n_max)


Time: 0.23496365547180176 for 10000 Contracts
Filename: script/best_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.3 MiB     22.3 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     24.2 MiB      1.9 MiB       50002       requests = [number for number in range(1, range_limit, 1)]
    10     24.2 MiB      0.0 MiB           1       n_max = 3
    11
    12     24.2 MiB      0.0 MiB           1       orders = Orders()
    13     24.3 MiB      0.1 MiB           1       orders.combine_orders(requests, n_max)


Time: 1.2665138244628906 for 50000 Contracts
Filename: script/best_performance/question2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     23.8 MiB     23.8 MiB           1   @profile
     8                                         def main(range_limit: int) -> None:
     9     26.4 MiB      2.6 MiB      100002       requests = [number for number in range(1, range_limit, 1)]
    10     26.4 MiB      0.0 MiB           1       n_max = 3
    11
    12     26.4 MiB      0.0 MiB           1       orders = Orders()
    13     26.5 MiB      0.1 MiB           1       orders.combine_orders(requests, n_max)


Time: 2.8542630672454834 for 100000 Contracts
```

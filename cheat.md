# AtCoderチートシート (Python 3)

## 標準入力の読込

### 文字列の読込

#### 1行に1個の文字列

##### 入力例

```bash
abc
```

##### コード

```python
S = input()   # type(S) = <class 'str'>
```

#### 1行に複数個の文字列

##### 入力例

```bash
abc def ghi
```

##### コード

```python
# listとして受け取る
S = input().split()   # >>> [abc, def, ghi]
# 文字列として受け取る
A, B, C = input().split()
print(A)   # >>> abc
```

### 数値の読込

#### 1行に1個の数値

##### 入力例

```bash
# 整数
12
# 小数
3.14
```

##### コード

```python
# 整数の場合
N = int(input())     # type(N) = <class 'int'>
# 小数の場合
N = float(input())   # type(N) = <class 'float'>
```

#### 1行に複数個の数値

##### 入力例

```bash
# 整数
1 2 3
```

##### コード

```python
# listとして受け取る
A = list(map(int, input().split()))   # >>> [1, 2, 3]
# 整数として受け取る
L, M, N = list(map(int, input().split()))
print(L)   # >>> 1
# 集合として読み込む
A = set(map(int, input().split()))   # >>> {1, 2, 3}
```

#### 複数行に1個の整数

##### 入力例

```math
\begin{array}{c}
N \\ 
A_{1} \\ 
\vdots \\ 
A_{N}
\end{array}
```

```bash
3
1
2
3
```

##### コード

```python
N = int(input())   # >>> 3
# A_1, ..., A_Nをlistとして読み込む場合
A = [int(x) for _ in range(N)]   # >>> [1, 2, 3]
# A_1, ..., A_Nを集合として読み込む場合
A = {int(x) for _ in range(N)}   # >>> {1, 2, 3}
```

#### 複数行に整数の組

##### 入力例

```math
\begin{array}{cc}
N & \space \\ A_{1} & B_{1}  \\ \vdots & \vdots \\ A_{N} & B_{N}
\end{array}
```

```bash
3
1 2
2 4
3 6
```

- 各行をtupleで読み込んでおくとsortの際に便利

##### コード

```python
N = int(input())   # >>> 3
L = [tuple(map(int, input().split())) for _ in range(N)]   # >>> [(1, 2), (2, 4), (3, 6)]
print(L[0])                                                # >>> (1, 2)
print(L[0][1])                                             # >>> 2
```

## 数学

### 順列・組み合わせ

```python
# 順列の総数（nPr）の計算
def perm(n, r):
  if n < 0 or r < 0 or n < r:
    return 0
  elif n == 0 or r == 0:
    return 1
  return perm(n, r - 1) * (n - r + 1)

# 組み合わせの総数（nCr）の計算
def comb(n, r):
  if n < r or n < 0 or r < 0:
    return 0
  r = min(r, n - r)
  if n == 0 or r == 0:
    return 1
  return (n - r + 1) * comb(n, r - 1) // r
```

### 最大公約数・最小公倍数

```python
# ユークリッドの互除法により，2つの整数m，nの最大公約数を求める．
def gcd(m, n):
  while n:
    m, n = n, m % n
  return m

# 2つの整数m，nの最小公倍数を求める．
def lcm(m, n):
  return m * n // gcd(m, n)
```

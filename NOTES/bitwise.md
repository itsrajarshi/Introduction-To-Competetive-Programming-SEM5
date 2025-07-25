# 🔧 Bitwise Operators in Python

Bitwise operators are used to perform operations on individual bits of integers. They are highly efficient and frequently used in low-level programming, cryptography, and competitive coding.

---

## 📋 Operator Reference Table

| Operator | Description           | Syntax  | Example (`x = 5`, `y = 3`) | Result       |
|----------|------------------------|---------|-----------------------------|--------------|
| `&`      | Bitwise AND            | `x & y` | `5 & 3 → 101 & 011`         | `1`          |
| `|`      | Bitwise OR             | `x | y` | `5 | 3 → 101 | 011`         | `7`          |
| `~`      | Bitwise NOT            | `~x`    | `~5 → ~00000101`            | `-6`         |
| `^`      | Bitwise XOR            | `x ^ y` | `5 ^ 3 → 101 ^ 011`         | `6`          |
| `>>`     | Bitwise Right Shift    | `x >> 1`| `5 >> 1 → 00000101 → 00000010` | `2`       |
| `<<`     | Bitwise Left Shift     | `x << 1`| `5 << 1 → 00000101 → 00001010` | `10`      |

---

## 🧠 Operator Breakdown

### `&` Bitwise AND
- Compares each bit of `x` and `y`
- Returns `1` if both bits are `1`
```python
print(5 & 3)  # Output: 1

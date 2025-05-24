# gstpy

A simple Python module to calculate GST (Goods and Services Tax) in both **inclusive** and **exclusive** modes.  
It provides clear outputs either as a list or as a formatted table.

---

## Features

- Calculate **inclusive GST** (GST already included in the given amount).
- Calculate **exclusive GST** (GST to be added to the base amount).
- Display results as a Python list or a nicely formatted table.
- Simple wrapper function `gstpy()` to handle both modes easily.

---

## Installation

```bash
pip install gstpy
```

## Usage
Import the module:

```python
from gstpy import gstpy
```
## Functions

### `inclusive(amount, gst_rate, output='list')`

Calculate GST when the tax is already included in the amount.

### `exclusive(amount, gst_rate, output='list')`

Calculate GST when the tax needs to be added to the base amount.

### `gstpy(amount, gst_rate, mode='exclusive', output='list')`

Wrapper function that calculates GST based on the selected mode.

## Parameters

- **amount** (float): The amount on which GST is to be calculated.
- **gst_rate** (float): GST percentage rate (e.g., 5, 12, 18, 28).
- **mode** (str): "inclusive" or "exclusive". Default is "exclusive".
- **output** (str): "list" returns a Python list, "table" prints a formatted table. Default is "list".

# Examples

## gstpy() : General GST calculator wrapper function.

```python
from gstpy import gstpy
```
# Exclusive GST example: Calculate GST on base amount ₹1000 at 18%
result = gstpy(amount=1000, gst_rate=18, mode="exclusive", output="list")
print(result)
# Output: [['Actual Amount', 1000], ['GST Amount', 180.0], ['Total Amount', 1180.0]]

# Inclusive GST example: Calculate GST included in ₹1180 at 18%, print as table
gstpy(amount=1180, gst_rate=18, mode="inclusive", output="table")

# Output:
# ╭───────────────────┬────────────╮
# │ Description       │   Amount(₹)│
# ╞═══════════════════╪════════════╡
# │ Actual Amount     │      1000  │
# │ GST Amount        │       180  │
# │ Total Amount      │      1180  │
# ╰───────────────────┴────────────╯

## Note

The `mode` and `output` parameters are optional. By default, `mode` is set to `"exclusive"` and `output` is set to `"list"`.

## `exclusive()` Function

```python
from gstpy import exclusive
```
# Calculate GST to be added to base amount ₹1000 at 18% rate
result = exclusive(amount=1000, gst_rate=18, output="list")
print(result)
# Output: [['Actual Amount', 1000], ['GST Amount', 180.0], ['Total Amount', 1180.0]]

# Display the result in tabular format
exclusive(amount=1000, gst_rate=18, output="table")

# Output:
# ╭───────────────────┬────────────╮
# │ Description       │   Amount(₹)│
# ╞═══════════════════╪════════════╡
# │ Actual Amount     │      1000  │
# │ GST Amount        │       180  │
# │ Total Amount      │      1180  │
# ╰───────────────────┴────────────╯

## Note

The `output` parameter is optional and, by default, is set to `"list"`.

## `inclusive()` Function

```python
from gstpy import inclusive
```
# Calculate actual and GST amounts from ₹1180 inclusive of 18% GST
result = inclusive(amount=1180, gst_rate=18, output="list")
print(result)
# Output: [['Actual Amount', 1000.0], ['GST Amount', 180.0], ['Total Amount', 1180.0]]

# Display the result in tabular format
inclusive(amount=1180, gst_rate=18, output="table")

## Note

The `output` parameter is optional and, by default, is set to `"list"`.

## GitHub Repository

You can find the source code and contribute to the project at the following link:

[GitHub Repository](https://github.com/ankush-dhingraa/gstpy)

## Connect with Us

For updates and support, connect with us on LinkedIn:

[LinkedIn Profile](https://www.linkedin.com/in/ankush-dhingraa/)
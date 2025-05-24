from tabulate import tabulate

# Headers used for tabular display
HEADERS = ["Description","Amount(₹)"]
# inclusive function for calculate inclusive GST
def inclusive(amount, gst_rate, output = "list"):
    """
    Calculate inclusive GST (tax already included in the given amount).

    Args:
        amount (float): Total amount including GST.
        gst_rate (float): GST rate percentage (e.g., 5, 12, 18, 28).
        output (str)(optional): "list" returns data as a list of lists,
                      "table" prints a formatted table.

    Returns:
        list: list data if output="list", else prints the table.
    """
    #calculate inclusive GST
    GST_amount = round((amount*gst_rate)/(100+gst_rate),2)
    actual_amount = round(amount - GST_amount,2)
    total_amount = round(GST_amount + actual_amount,2)
    data = [["Actual Amount",actual_amount],["GST Amount",GST_amount],["Total Amount",total_amount]]
    if output == "list":
        #return a list
        return data
    elif output.lower()=="table":
        #display data in tabular form
        display(data=data)

# exclusive function for calculate exclusive GST
def exclusive(amount, gst_rate, output = "list"):
    """
    Calculate exclusive GST (tax to be added to the base amount).

    Args:
        amount (float): Base amount excluding GST.
        gst_rate (float): GST rate percentage.
        output (str)(optional): "list" returns data as a list of lists,
                      "table" prints a formatted table.

    Returns:
        list: list data if output="list", else prints the table.
    """
    #calculate exclusive GST
    GST_amount = round((amount*gst_rate)/(100),2)
    total_amount = round(GST_amount + amount,2)
    data = [["Actual Amount",amount],["GST Amount",GST_amount],["Total Amount",total_amount]]
    if output == "list":
        #return a list
        return data
    elif output.lower()=="table":
        #display data in tabular form
        display(data=data)
def gstpy(amount, gst_rate, mode = "exclusive", output = "list"):
    """
    General GST calculator wrapper function.

    Args:
        amount (float): Amount to calculate GST on.
        gst_rate (float): GST rate percentage.
        mode (str): 'exclusive' or 'inclusive'.
        output (str): 'list' or 'table'.

    Returns:
        list: list data if output="list", else prints the table.
    """
    if mode.lower() == "exclusive":
        if output == "list":
            return exclusive(amount=amount,gst_rate=gst_rate,output=output)
        else:
            exclusive(amount=amount,gst_rate=gst_rate,output=output)
    elif mode.lower() == "inclusive":
        if output == "list":
            return inclusive(amount=amount,gst_rate=gst_rate,output=output)
        else:
            inclusive(amount=amount,gst_rate=gst_rate,output=output)

def display(data):
    """
    Helper function to print GST data in a table format using tabulate.

    Args:
        data (list): A list of [description, value] pairs to display.
    """
    #for display
    print(tabulate(data, HEADERS, tablefmt="rounded_grid"))
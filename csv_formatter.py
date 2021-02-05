# The Purpose of this module is to reformat dataframe column data that has been pulled from csv files that use mixed alpha numeric string representation of integers and floats. The functions herein are intended to be called on the values them selves within the context of pandas apply and replace methods. future updates may integrate for use on dataframe objects themselves. 

def pull_comma(csv_str: str)-> str:
  """For use on integer||float values represented by strings containing "," characters.
     Does not alter the notation or denomination of the value. ie: "1,000" will not become
     "1k" 
     input <-- str
     output --> str
  """
  if ',' in csv_str:
    csv_str = csv_str.split(',')
    csv_str = ''.join(csv_str)
    return csv_str
  else:
    return csv_str


def pull_denom(csv_str: str)-> str:
  """For use on integer||float values represented by strings denoting denomination with the use
     of an alpha-char such as "23k" Does not perform conversion to parts of another denomination.
     ie: "23k" does not become ".023" if you wanted parts of milions. transformation is literal.
     thus "23k" becomes "23000" also works for strings denoting '%' if '%' denoted at end of string

     input<-- str
     output--> str
  """
  if not csv_str.isnumeric():
    return csv_str[:-1] if csv_str[0].isnumeric() else 'Nan'
  else:
    return csv_str


def pull_currency(cvs_str):
  """For use on numeric strings that begin with a currency or denom char.

  """
  return cvs_str[1:] if cvs_str[1].isnumeric() else 0

 
 
    


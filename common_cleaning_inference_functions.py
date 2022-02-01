# Check dtype 
df[column].dtype

# Change dtype 
df[column] = df[column].astype(str) #can also convert to int, float, etc. 

# Specify dtype as percentage; convert dtype to n decimal points (in this case, 2) 

# Check for unique value
df['Identifier'].is_unique

# Drop Duplicates 
df = df.drop_duplicates(subset=['Column1','Column2'],keep='last')

# Removal of any extra white space (in a string) 
def remove_extra_white_space(string):
    try:
        string = " ".join(string.split())
    except:
        None
    return string

# Removal of certain prefixes 
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

# Removal of extra characters for scraped data
def remove_extra_characters(string):
    try:
        string = string.replace('\\n', " ")
        string = string.replace('\n', " ")
        string = string.replace('\\', " ")
        string = string.replace('\\t', " ")
        string = string.replace('\t', " ")
        string = string.replace('"', "")
    except:
        None

    return string

# Conversion to DateTime formats: 
# When the column is not in date-time format 
df['date'] = pd.to_datetime(df['date'], unit='ns',errors='coerce')
# Conversion to YYYY - MM - DD 
df.datetime = pd.to_datetime(df[datetime]).dt.strftime('%Y-%m-%d').astype('datetime64[ns]')

#removed special characters. 
df[column] = df[column].str.replace('\W', '')
 
  

#Pandas Solution using .title() method directly to create a new column
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['converted_text'] = user_content['content_text'].str.title()
    return user_content.rename(columns={'content_text':'original_text'})

#Another Pandas Solution
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

                    # change to title case with title() method
    user_content['converted_text'] = (
            user_content.content_text.apply(lambda x: x.title()))

                    # rename column per problem request
    return user_content.rename(columns={'content_text': 'original_text'})    

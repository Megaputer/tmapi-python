# KeywordsResponseKeywords

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | Normalized keyword | [optional] 
**negated** | **bool** | Indicates negation in the semantics of the word and returns the boolean values | [optional] 
**part_of_speech** | **str** | Part of speech of the keyword | [optional] 
**significance** | **float** | How distinct a particular keyword is for the explored text. Significance is calculated on a scale of 0,00 to 100,00. The greater the significance, the greater the chance that the concepts in the investigated data revolve around such a word.  | [optional] 
**support** | **int** | The number of different records containing the keyword | [optional] 
**frequency** | **int** | The number of times the keyword appears in the data | [optional] 
**positions** | [**list[KeywordsResponsePositions]**](KeywordsResponsePositions.md) | Keyword positions in text | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



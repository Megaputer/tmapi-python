# SentimentsResponseAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Either the speaker himself or another person (a group of people) whose opinion is shared. The subject of evaluation is not always mentioned in a text, especially when we deal with informal texts, such as forums, blogs and social network posts.  | [optional] 
**evaluation** | **str** | Implies the emotional judgment of a subject to some topic, an emotional reaction to something or the overall emotional tone of an utterance. Evaluation expresses an attitude of a subjeсt to a particular object, emotional response to something.  | [optional] 
**object** | **str** | It is something which is evaluated. Similar to the subject of evaluation, objects may not always be mentioned. | [optional] 
**head_object** | **str** | The main words in a phrase. | [optional] 
**degree** | **int** | It is used to refer to the degree of positive evaluation ranging from 1 to 5 (1-rather positivem 5 - extremely positive) and negative evaluation ranging from -1 to -5 (-1 rather negative, - 5 - extremely negative).  | [optional] 
**aspect** | **str** | It is a word or phrase that defines what characteristic of the object is evaluated. It allows users to summarize different ways of expressing the same entity in one thematic section.  | [optional] 
**confidence** | **float** | It represents measure of how sure TM API Server in its conclusion. Confidence is measured on scale of 0.0 to 1.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Map Reduce deploy on Hadoop

1. Explore a large-scale dataset
2. Process a large-scale dataset using MapReduce
3. Use Elastic MapReduce to run a MapReduce job on the cloud
4. Understand the benefits of frameworks such as MapReduce to analyze large volumes of data

## Big Data Analytics
Processing a single file sequentially like we did in the last module does not really answer the question of "What was the most popular page for the month of December 2015?" or "How many hits did any particular page get on a particular day?"

To be able to answer this we must:

* aggregate the view counts, and
* generate a daily timeline of page views for each article we are interested in.

In order to process such a large dataset (~65 GB compressed), we will setup an Elastic MapReduce job flow. You will have to write simple Map and Reduce functions or programs in the language of your choice.

In this module you will understand some of the key aspects of Elastic MapReduce (EMR) and run an Elastic MapReduce job flow. You will need to clearly understand the pricing and tagging model of EMR before we start.

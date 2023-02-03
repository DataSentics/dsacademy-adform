# DataSentics academy: Try work with different data

Previously you work with 'mostly' static data - for this task we have quite a lot of data from different days and it will grow larger. You should be able to handle that.

## Task description

On storage that you were using - `adapeuacadlakeg2dev` in container `01rawdata` is new section `Adform`. It contains four main different data sets - `Click`, `Event`, `Impression` and `Trackingpoint`. There are some connections between these data sets and you should be able to figure out how to merge them into one table.

Also, it shouldn't be too simple and easy - there are also some `metadata` for this previous data sets. Try to find out how to enrich your main data sets using these metadata.

However, there are many columns that has no meaning at all, we probably don't need them anymore. Also, when you will do "merge" these two data source, be aware of duplicities in rows and columns.

But there are also lot of columns with added meaning - try to find them and separate them as "most information handling column", same as "the most useless" will be removed.

Be ready that data should be expanding each day - that's why all of them are inside folder `Increment` - but no more often. Data are mostly raw, without further processing.

### What to do?

- Create a new metastore database, called `<your_name>_adform`, in which all your tables will reside.
- All data should be saved in your azure storage container. You can organize the data in the container in any way you see fit. 
- Create a multi-hop architecture using pyspark.
- Name the tables in some sensible ways, like `silver_...`.
- Split your solution into multiple notebooks. It is often good to create a separate notebook for each output table. I.e., each notebook should write just one table (but can read multiple inputs). And the name of the notebook can be derived from the name of the output table.
- Create a parsed layer = the raw data converted to Delta.
- Create a cleansed layer = clean the data. (Inspecting the data, in what ways it is unclean, can be done in a separate notebook, which will not be used in the ETL pipeline.)
- Create a common data model layer = all the data in a 3rd normal form, from which aggregations and other custom analytical queries can be done. (hint: here the PII data will probably cease to be a separate table)
- Create a gold layer: Create tables with aggregate statistics for useful columns - you probably see these data for the first time (it's fine) but you should be able to present your own point of view - what's important from your perspective
- Orchestrate the whole ETL pipeline using a multi-task databricks job (workflow). Do not create a schedule for it, but think about how and when would you schedule it. You can store the definition of this job also as code as part of your solution. The notebooks can be e.g. in a folder called `src` and the job in a folder called `databricks-infra`.
- Because data will be expanding "endlesly" create store them using partitioning (use best column(s) ) or/and bucketing.
- Should there be streaming or not?

And more:
- Identify how many unique bots are there (if any) and how many non-bots for each day
 - Somewhere in data you can find `PublisherDomain` (that's place, where advertisement was shown and we have data about it) - find TOP 10 pages that shown any advert for any day, for any week and for any month
- There are also `UserSettingsVars` and it contains `countryid` - even without any decoding table, find again TOP 10 countries from where people went to our pages
- Youu can find interesting values inside `metadata_devices` - aggregate them and show graph(s) for whole dataset that show dependency using specific device in specific hour

### Technical notes

- Create and work in your own branch, derived from the `main` branch.
- You will submit your work by creating a pull request from your branch to `main` (and letting someone from the academy team know about it:-)).
  - Afterwards, someone will do a code review in the pull request. You will likely need to modify your code based on the review. Maybe you will go through several rounds of review :)
  - When all the review comments are resolved, Github will allow you to do the merge to `main`, but please DO NOT MERGE your branch to `main`! It doesn't make sense in our dummy project :) (To prevent this, the repo is set to require two approvals of the PR..)
  - When the project is approved by us, please also delete your (ONLY YOUR) databases and files in Databricks and cloud storage.
- Info to provided data: it comes from data provider that collect them after visitor of web pages provide consent to collect data about him in form of cookies. And as you will see later in data, there are quite a lot of things to be found.
- There is not code validation - try your best on your own :)
- We have prepared `src` folder - create there your own folder INSIDE this `src` like `<your_name>` and put everything inside :)

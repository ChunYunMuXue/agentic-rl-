write some record

# Discussion on Mar 12

## TODO

- Figure out the dataset **BrowseComp-Plus**
  
  - [Leaderboard](https://huggingface.co/spaces/Tevatron/BrowseComp-Plus)
  - [GitHub](https://github.com/texttron/BrowseComp-Plus)
  - [HuggingFace dataset](https://huggingface.co/datasets/Tevatron/browsecomp-plus)
  
  - How to see the questions/answers?  
      > has 830 line datas all,it is put at ./data,but maybe its so big
      > I take one line for demo,could see that it has so many materials 
      > Its structure : [query\_id\ ,\ query\ ,\ answer\ ,\ gold\_docs\ :\ \{[docid,text,url],[...],[...],[...]\}]
  - How to see the reference materials?
      > in the question structure,there is "gold_docs"
  - How to build an agent to use this dataset (through HuggingFace or other methods)?
  
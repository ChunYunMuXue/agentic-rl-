write some record

# Discussion on Mar 12

## TODO

- Figure out the dataset **BrowseComp-Plus**
  
  - [Leaderboard](https://huggingface.co/spaces/Tevatron/BrowseComp-Plus)
  - [GitHub](https://github.com/texttron/BrowseComp-Plus)
  - [HuggingFace dataset](https://huggingface.co/datasets/Tevatron/browsecomp-plus)
  
  - How to see the questions/answers?  
      > has 830 line datas all,it is put at ./data,but maybe its so big<br>
      > I take one line for demo,could see that it has so many materials <br>
      > Its structure : [query\_id ,quer,answer,gold\_docs:\{[docid,text,url],[...],[...],[...]\}]
  - How to see the reference materials?
      > In the question structure, there is a field "gold\_docs", which is hidden from the agent and manually annotated. <br>
      > The agent is only provided with the query text and a large corpus, Tevatron/browsecomp-plus-corpus.      
      
  - How to build an agent to use this dataset (through HuggingFace or other methods)?

  
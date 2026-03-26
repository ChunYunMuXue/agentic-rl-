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
      > In the question structure, there is a field "gold\_docs", which is hidden from the agent and manually annotated<br>
      > The agent is only provided with the query text and a large corpus, **Tevatron/browsecomp-plus-corpus** <br>
      > I take some demos in **./data/corpus\_demo\_3.jsonl**

  - How to build an agent to use this dataset (through HuggingFace or other methods)?
      > I think we could use the BrowseComp-Plus/search_agent as example<br>
      > need llm agent + tool (retrieval,and using that as local network) <br>
      > has done the running <br>
      > there are some demos in the github by tevatron.
      > and have done one run with Qwen1.7B


What is the SOTA and main agentic designs used on this dataset?
– Chen et al. (2026b) (retrieval design,with code) done
– Kariyappa and Suh (2026) (KV cache,memory,no open) done
– Chen et al. (2026a) (evaluation, no open) done
– He et al. (2026) (evaluation, no open) waiting


References
Y. Chen, J. Jiang, J. Liu, Y. Zhang, X. Guo, and I. King. Trace: Trajectory-aware comprehensive
evaluation for deep research agents. arXiv preprint arXiv:2602.21230, 2026a.
Z. Chen, X. Ma, S. Zhuang, J. Lin, A. Asai, and V. Zhong. Agentir: Reasoning-aware retrieval for
deep research agents. arXiv preprint arXiv:2603.04384, 2026b.
Z. He, Y. Wang, C. Zhi, Y. Hu, T.-P. Chen, L. Yin, Z. Chen, T. A. Wu, S. Ouyang, Z. Wang, et al.
Memoryarena: Benchmarking agent memory in interdependent multi-session agentic tasks. arXiv
preprint arXiv:2602.16313, 2026.
S. Kariyappa and G. E. Suh. Sidequest: Model-driven kv cache management for long-horizon agentic
reasoning. arXiv preprint arXiv:2602.22603, 2026
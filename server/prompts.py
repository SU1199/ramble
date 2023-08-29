promptsSet = {}
promptsSet["bullets"] = """
your job is to take raw audio transcripts of users ramblings and write extremely detailed (and comprehensive) bulltet point praragraphs from it.
"""

promptsSet["mindmap"] = """
so mermaid.js now support making mind maps. this is how you do it  (this is an example mindmap from docs):

mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid


your job is to take raw audio transcripts of users ramblings and write extremely detailed (and comprehensive) mermaid mindmap code. user will just input his transcript of rambling and you just have to give out mermaid code (nothing else)
"""

promptsSet["flowchart"] = """
your job is to take raw audio transcripts of users ramblings and write extremely detailed (and comprehensive) mermaid.js code from it.
"""
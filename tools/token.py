class Token:
  def word_tokenisation():
      text = """There are, multiple ways we can perform tokenization on given text data. We can choose any method based on langauge, library and purpose of modeling."""
      # Split text by whitespace
      special_characters = ['!','"','#','$','%','&','(',')','*','+','-','/',':',';','<','=','>','@','[','\\',']','^','_','`','{','|','}','~','\t', ',', '.',]
      for i in special_characters : 
        text = text.replace(i, '')  
      tokens = text.split()
      print(tokens)

  def sentance_tokenisation():
      text = """Founded in 2002, SpaceX's mission is to enable humans to become a spacefaring civilization and a multi-planet species by building a self-sustaining city on Mars. In 2008, SpaceX's Falcon 1 became the first privately developed liquid-fuel launch vehicle to orbit the Earth."""
      tokens = text.split('. ')  
      # print(tokens)  

  word_tokenisation()
  sentance_tokenisation()
# TODO: Take arguments from command line

gloss_file = 'Glossary.md'

target_file = 'Wikified-Rules.md' 

glosses = Array.new()

# Collect the glosses from each h1 line.
# TODO: Probably should be more careful to strip whitespace
File.foreach(gloss_file) do |line|
  if line.match("^#.*")
    glosses.push(/(?<![\[\(])#{line[2..-2]}(?![\]\)])/i)
  end
end

re = Regexp.union(glosses)

File.foreach(target_file) do |line|
  line = line.gsub(re) {|match| "[[#{match}|Glossary##{match.downcase}]]"}
  puts line
end

import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

	return [word for word in words if re.search(regex, word)]

print get_matching_words(r".*v.*")
print''
print get_matching_words(r".*ss.*")
print''
print get_matching_words(r"e$")
print''
print get_matching_words(r".*b.b.*")
print''
print get_matching_words(r".*b.+b.*")
print''
print get_matching_words(r".*b.*b.*")
print''
print get_matching_words(r".*a.*e.*i.*o.*u*")
print''
print get_matching_words(r"[regular expressions]")
print''
print get_matching_words(r"(.)\1")
print''
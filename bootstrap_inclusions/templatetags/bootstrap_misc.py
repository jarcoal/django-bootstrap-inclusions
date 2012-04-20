from django import template
register = template.Library()


@register.inclusion_tag('bootstrap_inclusions/misc/icon.html')
def icon(id, white=False):
	"""
	Generates a Bootstrap Icon.
	
	:param id: The ID of the icon (ex: "plus", "picture")
	:param white: If white should be used.  Pass in anything that resolves to True.
	"""
	return { 'id': id, 'white': white }


@register.inclusion_tag('bootstrap_inclusions/misc/label.html')
def label(text, kind=''):
	"""
	Generates a Bootstrap Label.
	
	:param text: Text to appear in the label.
	:param kind: Kind of label: success, warning, important, info, inverse, or leave blank for default.
	"""
	return { 'text': text, 'kind': kind, }
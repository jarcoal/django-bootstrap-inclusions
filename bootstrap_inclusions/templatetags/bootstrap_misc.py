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
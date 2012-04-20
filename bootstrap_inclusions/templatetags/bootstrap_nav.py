from django import template
register = template.Library()


@register.inclusion_tag('bootstrap_inclusions/nav/breadcrumb.html')
def breadcrumb(units):
	"""
	Generates a Bootstrap Breadcrumb.  Last unit is marked as active.
	
	:param units: A list of lists/tuples formatted like this: [('Label', 'URL'), ('Label', 'URL',), ...]
	"""
	return { 'units': units, }
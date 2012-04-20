from django import template
register = template.Library()


@register.inclusion_tag('bootstrap_inclusions/fields/horizontal.html')
def horizontal_field(field, inline=None):
	"""
	Generates a field row rendered in Bootstrap horizontal layout.
	"""
	
	widget_type = field.field.widget.__class__.__name__.upper()
	
	if inline is None:
		inline = False if widget_type == 'CHECKBOXINPUT' else True
	
	return { 'field': field, 'widget_type': widget_type, 'inline': inline, }
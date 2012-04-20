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


@register.inclusion_tag('bootstrap_inclusions/misc/badge.html')
def badge(num, kind=''):
	"""
	Generates a Bootstrap Badge.
	
	:param num: Number to appear in badge.
	:param kind: Kind of badge: success, warning, error, info, inverse, or leave blank for default.
	"""
	return { 'num': num, 'kind': kind, }


@register.inclusion_tag('bootstrap_inclusions/misc/alert.html')
def alert(text, kind='', close=True):
	"""
	Generates a Bootstrap Alert.
	
	:param text: Text to appear in the alert.
	:param kind: Kind of alert: success, error, info, or leave blank for default.
	:param close: Pass in 0 to remove close button.
	"""
	return { 'text': text, 'kind': kind, 'close': close, }


@register.inclusion_tag('bootstrap_inclusions/misc/alert_block.html')
def alert_block(header, text, kind='', close=True):
	"""
	Generates a Bootstrap Alert.
	
	:param header: Text to appear in alert header.
	:param text: Text to appear in the alert.
	:param kind: Kind of alert: success, error, info, or leave blank for default.
	:param close: Pass in 0 to remove close button.
	"""
	return { 'header': header, 'text': text, 'kind': kind, 'close': close, }
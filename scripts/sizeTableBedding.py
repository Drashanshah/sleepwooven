# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import productDef as pd
import productCollection.bedding as bedding

def getTagTh(content):
	# returns th tag with content
	style = 'padding: 15px; border: 1px solid #ddd; text-align: center; font-weight: bold;'
	return '''<th style="{}">{}</th>'''.format(style, content)

def getTagTd(content):
	# returns td tag with content
	style = 'padding: 15px; border: 1px solid #ddd; text-align: center;'
	return '''<td style="{}">{}</td>'''.format(style, content)

def getTagTr(content):
	# returns th tag with content
	return '''<tr>{}</tr>'''.format(content)

def getTagThead(content):
	# returns td tag with content
	return '''<thead>{}</thead>'''.format(content)

def getTagTable(content, lang):
	# returns table tag
	style = "width: 100%;"

	if lang is 'chi':
		return '''<table id="sleepwooven-sizing-cm-chi" class="" style="{}">{}</table>'''.format(style, content)

	return '''<table id="sleepwooven-sizing-cm" class="" style="{}">{}</table>'''.format(style, content)



def getColumnContents(columnArr):
	#  return array the columns will appear, will accept custom orders
	if not columnArr:
		return [bedding.duvetCover, bedding.fittedSheet, bedding.flatSheet, bedding.pillowcase ]

	return columnArr

def getRowContents():
	# return array the columns will appear
	rows = [pd.TWIN, pd.FULL, pd.QUEEN, pd.KING]

	return rows

def getDimensionNote(lang='eng'):
	# return notes for table
	inputStr = pd.dimensionNote.get(lang)
	return '''<p class="dimension-info">{}</p>'''.format(inputStr)

def getTagBold(content):
	return '''<b>{}</b>'''.format(content)

def getTableHeaderRow(lang, columnArr=None):
	# make a table header row
	r = ''
	columns = getColumnContents(columnArr)

	# first column is mattress size:
	r += getTagTh(bedding.mattress.get(lang))

	for i in columns:
		r += getTagTh(i.get(lang))

	# wrap in tr tag
	trTag = getTagTr(r)

	# wrap in thead
	return getTagThead(trTag)



# size display preference, look for sizes in a particular order
# bedding is in cm first
# soap is in grams or g 

sizePreference = ['cm', 'g']

def getTableRows(lang, columnArr=None):
	# returns size orders
	r = ''
	columns = getColumnContents(columnArr)
	rows = getRowContents()

	for size in rows:
		row = ''
		# string output for size of mattress
		sizeName = size.get(lang)

		# print 'sizeName', sizeName, getTagTd(sizeName)
		row += getTagTd(sizeName)

		for prod in columns:
			# key for productName, i.e. 'fittedSheet'
			k = prod.get('lookup')

			# size of the product
			for pref in sizePreference:
				if pref in size.get(k):
					prodSize = size.get(k).get('cm')
					row += getTagTd(prodSize)
					break

			# print 'k', k, prodSize, getTagTd(prodSize)

		# wrap in tr tag
		r += getTagTr(row)

	return r


			

def getTableByLangColArr(lang='eng', columnArr=None):
	r = getTableHeaderRow(lang, columnArr)
	r += getTableRows(lang, columnArr)

	return getDimensionNote(lang) + getTagTable(r, lang)




# examples of use:

# print getTableByLangColArr(lang='eng')
# print getTableByLangColArr(lang='chi', columnArr = [bedding.fittedSheet, bedding.pillowcase])



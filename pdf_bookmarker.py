#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:17:39 2024

@author: matthew
"""

from PyPDF2 import PdfReader, PdfWriter
import sys

input_path = sys.argv[1]
output_path = f'{sys.argv[1].removesuffix(".pdf")}_bookmarked.pdf'

reader = PdfReader(input_path)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

#%% Oxford MYP3
"""
title = writer.add_outline_item('Title', 0)
contents = writer.add_outline_item('Contents', 4) # Add 5 to in-book numbers
number = writer.add_outline_item('1 Number: discoveries and developments', 9)
writer.add_outline_item('Unit summary', 38 + 7, number)
writer.add_outline_item('Unit review', 40 + 7, number)
writer.add_outline_item('Summative assessment', 45 + 7, number)


triangles = writer.add_outline_item('2 Triangles: principles, processes and solutions', 55)
writer.add_outline_item('Unit summary', 89 + 7, triangles)
writer.add_outline_item('Unit review', 90 + 7, triangles)
writer.add_outline_item('Summative assessment', 97 + 7, triangles)


linear_relationships = writer.add_outline_item('3 Linear relationships: impact of human decision-making', 107)
writer.add_outline_item('Unit summary', 139 + 7, linear_relationships)
writer.add_outline_item('Unit review', 141 + 7, linear_relationships)
writer.add_outline_item('Summative assessment', 148 + 7, linear_relationships)


shapes = writer.add_outline_item('4 3D shapes: products, processes and solutions', 159)
writer.add_outline_item('Unit summary', 192 + 7, shapes)
writer.add_outline_item('Unit review', 193 + 7, shapes)
writer.add_outline_item('Summative assessment', 199 + 7, shapes)


bivariate_data = writer.add_outline_item('5 Bivariate data: what it means to be human', 209)
writer.add_outline_item('Unit summary', 242 + 7, bivariate_data)
writer.add_outline_item('Unit review', 244 + 7, bivariate_data)
writer.add_outline_item('Summative assessment', 252 + 7, bivariate_data)


geometry = writer.add_outline_item('6 Geometric transformations: expressing beliefs and values', 261)
writer.add_outline_item('Unit summary', 298 + 7, geometry)
writer.add_outline_item('Unit review', 300 + 7, geometry)
writer.add_outline_item('Summative assessment', 311 + 7, geometry)


linear_systems = writer.add_outline_item('7 Linear systems: social entrepreneurship', 321)
writer.add_outline_item('Unit summary', 350 + 7, linear_systems)
writer.add_outline_item('Unit review', 351 + 7, linear_systems)
writer.add_outline_item('Summative assessment', 355 + 7, linear_systems)


writer.add_outline_item('Answers', 365)
writer.add_outline_item('Index', 407)
"""

#%% Oxford MYP4-5

heading = writer.add_outline_item('Title', 0)
contents = writer.add_outline_item('Contents', 5)


heading = writer.add_outline_item('1 Being Specific', 2 + 8)
writer.add_outline_item('1.1 Problem Solving', 4 + 8, heading)
writer.add_outline_item('1.2 The number system', 20 + 8, heading)
writer.add_outline_item('1.3 Laws of exponents and scientific notation', 41 + 8, heading)
writer.add_outline_item('1.4 Units and Measurement', 50 + 8, heading)
writer.add_outline_item('1.5 Surds, roots and radicals', 66 + 8, heading)
writer.add_outline_item('1.6 Absolute value', 80 + 8, heading)

heading = writer.add_outline_item('2 Decisions, decisions', 92 + 8)
writer.add_outline_item('2.1 Making generalizations', 94 + 8, heading)
writer.add_outline_item('2.2 Coordinate geometry', 104 + 8, heading)
writer.add_outline_item('2.3 Modelling: Linear equations and systems of linear equations', 123 + 8, heading)

heading = writer.add_outline_item('3 Back to the beginning', 138 + 8)
writer.add_outline_item('3.1 Relations and functions', 140 + 8, heading)
writer.add_outline_item('3.2 Quadratic expressions', 162 + 8, heading)
writer.add_outline_item('3.3 Representing quadratic functions', 177 + 8, heading)
writer.add_outline_item('3.4 Solving quadratic equations', 200 + 8, heading)

heading = writer.add_outline_item('4 Mathematically speaking', 218 + 8)
writer.add_outline_item('4.1 Set operations and Venn diagrams', 220 + 8, heading)
writer.add_outline_item('4.2 Probability of single and combined events', 234 + 8, heading)

heading = writer.add_outline_item('5 Spacious interiors', 260 + 8)
writer.add_outline_item('5.1 Surface area and volume', 262 + 8, heading)
writer.add_outline_item('5.2 Geometric transformations', 277 + 8, heading)

heading = writer.add_outline_item('6 A whole range of things', 304 + 8)
writer.add_outline_item('6.1 Univariate statistics', 306 + 8, heading)
writer.add_outline_item('6.2 Quantifying data', 326 + 8, heading)
writer.add_outline_item('6.3 Histograms', 348 + 8, heading)

heading = writer.add_outline_item('7 How do they measure up?', 362 + 8)
writer.add_outline_item('7.1 The right triangle', 364 + 8, heading)
writer.add_outline_item('7.2 Properties of circles', 379 + 8, heading)
writer.add_outline_item('7.3 Circle theorems 1', 394 + 8, heading)
writer.add_outline_item('7.4 Circle theorems 2', 408 + 8, heading)

heading = writer.add_outline_item('8 What comes next?', 416 + 8)
writer.add_outline_item('8.1 Sequences', 418 + 8, heading)
writer.add_outline_item('8.2 Rearranging formulae and proportion', 432 + 8, heading)

heading = writer.add_outline_item('So, what do you think?', 458 + 8)
writer.add_outline_item('9.1 Sampling techniques', 460 + 8, heading)
writer.add_outline_item('9.2 Bivariate data', 477 + 8, heading)


#heading = writer.add_outline_item(title,  + 8)
#writer.add_outline_item('',  + 8, heading)

writer.add_outline_item('Index', 488 + 8)


with open(output_path, 'wb') as output_pdf:
    writer.write(output_pdf)

print('Bookmarks added!')

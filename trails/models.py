from django.db import models
import bs4
import requests

from plotly.offline import plot
import plotly.graph_objects as go

#Get the trail data from the URL
class trailModel(models.Model):
  #Method to get the trail names from the URL and store it in a list
  def getTrailData():
    trails = requests.get("https://trails.colorado.gov/featured-routes") #Get the html page for the trails using requests
    trails.raise_for_status() #Make sure the URL is valid
    trailPage = bs4.BeautifulSoup(trails.text, features="html.parser") #Parse the page to get the html with beautiful soup

    locations = [] #List to keep track of the locations that have scenic listed with them
    icons = (trailPage.find_all("img", {"title": "Scenic"})) #Find all the titles within the images listed as scenic
    for icon in icons: #Add the scenic locations to the locations list
        locations.append(icon.findParent().findParent().findParent().findParent().findParent().find("span", {"class":"result-list-item-label"}).text)
    return locations #Return the list

#Get the binocular data from the URL
class binocModel(models.Model):
  #Method to get the binocular data from the URl and store it in a dictionary
  def getBinocData():
    binoculars = requests.get("https://www.opticsplanet.com/binoculars.html") #Get the html page for the binoculars using requests
    binoculars.raise_for_status() #Make sure the binocular URL is valid
    binocPage = bs4.BeautifulSoup(binoculars.text, features="html.parser") #Parse the page to get the html

    binocDict = {} #Dictionary to keep track of the binocs and the price associated with them
    binocs = (binocPage.find_all("div", {"data-grid-name": "Category Products"})) #Get the html for all the binoculars on the first page
    for binoc in binocs: #Add the binoculars to a dictionary with the name as the key and the price as the value
        if(binoc.find("span", {"class": "variant-price grid__price"})): 
            binocDict[binoc.find("span", {"class": "grid__text"}).text] = float((binoc.find("span", {"class": "variant-price grid__price"}).text)[2:-2].replace(',', ''))
    return binocDict #Return the dictionary

#Class to display the binocular prices in a graph with plotly
class displayData(models.Model):
  #Method to display the prices of the binoculars in the graph
  def getBinocPrices():
    xValues = list(binocModel.getBinocData().values())
    yValues = [i for i in range(1, 100)]
    fig = go.Figure(data=go.Histogram(x=sorted(xValues), y=yValues))
    fig.update_layout(xaxis_title="Price ($)", yaxis_title="Count (Binoculars)")
    plot_div = plot({'data': fig}, output_type = 'div')
    return plot_div #Return the plot
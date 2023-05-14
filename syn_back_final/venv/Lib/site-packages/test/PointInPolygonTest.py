import unittest
import geopandas as gpd
import PointInPolygon as pnp

### TEST

class FunctionsTest(unittest.TestCase):

  def testGeo2Array(self):
    geodf = gpd.read_file('./test/test1.geojson')
    geoarray = pnp.Geo2Array(geodf['geometry'].values[0])
    length = len(geoarray)
    self.assertEqual(length, 7739)
    print('Geo convert to array is correct')
    
  def testMultiPolygon2Polygon(self):
    geodf = gpd.read_file('./test/test.geojson')
    length = len(geodf)
    self.assertEqual(length, 10)
    df = pnp.MultiPolygon2Polygon(geodf)
    length = len(df)
    self.assertEqual(length, 22)
    print('Multipolygon convert to array is correct')
  
  def testPointOnBorder(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(5,7)
    result = pnp.PointInPolygon(t2, t1)
    self.assertTrue(result)
    print('Point on border is correct')
  
  def testPointInPolygon(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(5,6)
    result = pnp.PointInPolygon(t2, t1)
    self.assertTrue(result)
    print('Point inside of polygon is correct')

  def testPointOutPolygon(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(4,7)
    result = pnp.PointInPolygon(t2, t1)
    self.assertFalse(result)
    print('Point outside of polygon is correct')
  
  def testMinValueX(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(2,4)
    result = pnp.minValue(t1, 0)
    self.assertEqual(result, t2)
    print('Min Value X is correct')

  def testMinValueY(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(4,2)
    result = pnp.minValue(t1, 1)
    self.assertEqual(result, t2)
    print('Min Value Y is correct')

  def testMaxValueX(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(9,6)
    result = pnp.maxValue(t1, 0)
    self.assertEqual(result, t2)
    print('Max Value X is correct')

  def testMaxValueY(self):
    t1=[(2,4),(4,2),(5,3),(6,4),(8,5),(9,6),(5,7),(2,6)]
    t2=(5,7)
    result = pnp.maxValue(t1, 1)
    self.assertEqual(result, t2)
    print('Max Value Y is correct')

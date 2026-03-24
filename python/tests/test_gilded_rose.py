# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    # 测试1：普通物品每天品质降低1
    def test_normal_item_quality_decreases_by_one(self):
        items = [Item("normal", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(19, items[0].quality)

    # 测试2：Aged Brie 品质每天增加1
    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(21, items[0].quality)

    # 测试3：Sulfuras 品质永远不变
    def test_sulfuras_quality_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)

    # 测试4：Conjured 物品品质每天降低2（原始代码未实现，会失败）
    def test_conjured_item_quality_decreases_by_two(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(18, items[0].quality)

if __name__ == '__main__':
    unittest.main()

    # Test 5: Normal item degrades by 2 after sell date
    def test_normal_item_degrades_twice_after_sell_date(self):
        items = [Item("normal", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    # Test 6: Quality is never negative
    def test_quality_never_negative(self):
        items = [Item("normal", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    # Test 7: Aged Brie quality does not exceed 50
    def test_aged_brie_quality_max_50(self):
        items = [Item("Aged Brie", 10, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

    # Test 8: Backstage passes quality drops to 0 after concert
    def test_backstage_passes_quality_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    # Test 9: Conjured item degrades by 4 after sell date
    def test_conjured_degrades_twice_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(6, items[0].quality)

    # Test 10: Sulfuras sell_in never changes
    def test_sulfuras_sell_in_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(10, items[0].sell_in)

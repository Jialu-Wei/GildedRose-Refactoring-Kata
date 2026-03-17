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

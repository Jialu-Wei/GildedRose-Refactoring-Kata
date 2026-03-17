# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# ── Strategy 基类 ──────────────────────────────────────────
class UpdateStrategy:
    def update(self, item):
        raise NotImplementedError


# ── 普通物品：每天-1，过期后-2，最低0 ──────────────────────
class NormalStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)


# ── Aged Brie：每天+1，最高50 ──────────────────────────────
class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        item.quality = min(50, item.quality + 1)


# ── Sulfuras：永不改变 ─────────────────────────────────────
class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        pass  # 什么都不做


# ── Backstage passes：临近演出涨价，过期归零 ───────────────
class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)


# ── Conjured：每天-2，过期后-4，最低0 ─────────────────────
class ConjuredStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)


# ── GildedRose：根据物品名称选择策略 ──────────────────────
class GildedRose(object):
    STRATEGIES = {
        "Aged Brie": AgedBrieStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
        "Conjured Mana Cake": ConjuredStrategy(),
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.STRATEGIES.get(item.name, NormalStrategy())
            strategy.update(item)

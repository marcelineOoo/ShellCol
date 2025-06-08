#!/usr/bin/env python3
import sys
from colormath.color_objects import sRGBColor, HSVColor, HSLColor
from colormath.color_conversions import convert_color
import re

def ask_choice(label, choices):
    print(f"\n{label}")
    for i, name in enumerate(choices, 1):
        print(f"{i}: {name}")
    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(choices):
                return choices[choice - 1]
        except ValueError:
            pass
        print("Invalid choice, try again.")

def format_output(color, fmt):
    if fmt == "hex":
        rgb = convert_color(color, sRGBColor)
        r = int(rgb.rgb_r * 255)
        g = int(rgb.rgb_g * 255)
        b = int(rgb.rgb_b * 255)
        return f"#{r:02X}{g:02X}{b:02X}"

    elif fmt == "rgb":
        rgb = convert_color(color, sRGBColor)
        r = int(rgb.rgb_r * 255)
        g = int(rgb.rgb_g * 255)
        b = int(rgb.rgb_b * 255)
        return f"rgb({r}, {g}, {b})"

    elif fmt == "hsl":
        hsl = convert_color(color, HSLColor)
        h, s, l = hsl.get_value_tuple()
        return f"hsl({round(h, 2)}, {round(s * 100, 2)}%, {round(l * 100, 2)}%)"

    elif fmt == "hsv":
        hsv = convert_color(color, HSVColor)
        h, s, v = hsv.get_value_tuple()
        return f"hsv({round(h, 2)}, {round(s * 100, 2)}%, {round(v * 100, 2)}%)"

    else:
        raise ValueError(f"Unknown format: {fmt}")

def parse_percentage_or_float(s):
    s = s.strip()
    if s.endswith('%'):
        return float(s[:-1]) / 100.0
    else:
        return float(s)

def parse_input(fmt, value):
    value = value.strip()
    if fmt == "hex":
        value = value.lstrip("#")
        if len(value) != 6:
            raise ValueError("Hex value must be 6 digits")
        r = int(value[0:2], 16)
        g = int(value[2:4], 16)
        b = int(value[4:6], 16)
        return sRGBColor(r / 255, g / 255, b / 255)

    elif fmt == "rgb":
        nums = [int(x) for x in re.findall(r'\d+', value)]
        if len(nums) != 3:
            raise ValueError("RGB requires 3 integers")
        return sRGBColor(nums[0] / 255, nums[1] / 255, nums[2] / 255)

    elif fmt in ("hsl", "hsv"):
        parts = [x.strip() for x in value.strip("()").split(",")]
        if len(parts) != 3:
            raise ValueError(f"{fmt.upper()} requires 3 values")
        h = float(parts[0])
        s = parse_percentage_or_float(parts[1])
        l_or_v = parse_percentage_or_float(parts[2])
        if fmt == "hsl":
            return HSLColor(h, s, l_or_v)
        else:
            return HSVColor(h, s, l_or_v)

    else:
        raise ValueError(f"Unknown input format: {fmt}")

def main():
    print("🎨 Quick and easy color converter — Press Ctrl+C to quit.")
    formats = ["hex", "rgb", "hsv", "hsl"]

    while True:
        try:
            source_fmt = ask_choice("What is the starting format?", formats)
            target_fmt = ask_choice("What is the target format?", formats)

            if source_fmt == target_fmt:
                print("⚠️  Source and target formats are identical, nothing to convert.\n")
                continue

            examples = {
                "hex": "#FF8800",
                "rgb": "(255, 136, 0)",
                "hsl": "(40, 100%, 50%)",
                "hsv": "(40, 100%, 100%)"
            }
            print(f"Enter the color in {source_fmt.upper()} format (e.g., {examples[source_fmt]})")
            raw_input_color = input("> ").strip()

            try:
                color_obj = parse_input(source_fmt, raw_input_color)
                result = format_output(color_obj, target_fmt)
                print(f"\n✅ Result: {result}\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")

        except KeyboardInterrupt:
            print("\n👋 Bye!")
            sys.exit(0)

if __name__ == "__main__":
    main()

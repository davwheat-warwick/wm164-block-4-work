# WM164 Smart Solutions Development I / Block 4 / Monday

## Homework

### Unicode and ASCII

ASCII (American Standard Code for Information Interchange) was one of the first standardised text encoding systems. It uses 7 bits to store up to 128 different characters in a computer system. The main limiting factor is that there is only 128 possible characters, which is nowhere near enough to store everything for all languages across the globe, in addition to various pictograms, such as emoji.

Because of this, the Unicode Consortium was established in order to facilitate a newer and more inclusive text encoding standard, which is now used almost exclusively by computers. This uses an infinite number of bytes per character, depending on when it was added to Unicode. Unicode is backwards compatible with ASCII since it utilises the same first 128 characters before then moving to its new additions.

The most common way to encoding Unicode characters is with UTF-8, which uses groups of 8 bits to encode glyphs.

```
0... .... refers to a single ASCII glyph
```

For non-ASCII characters, the first few bits of an encoded glyph state how many bytes need to be read to decode the character.

```
110. .... one byte follows this
1110 .... two bytes follow this
1111 0... three bytes follow this
```

Then every byte that follows one of these "start bytes" is as follows:

```
10.. .... continuation of a multi-byte glyph
```

#### Example

As an example, 😭 is represented by `U+1F62D`. This means that the bits used to encode this character must add up to `128557`.

128557 is greater than 127, so this isn't an ASCII character. This means that we know it will be multiple bytes to represent this character.

```
0x1F62D = 0b11111011000101101

10.. .... continuation of a multi-byte glyph

The last 6 bits of 0x1F62D are 101101, therefore the last byte of the emoji is 10101101
```

```
new remaining = 0b11111011000......

There are 11 bits left to encode. A 'one or more' starting byte encodes 5 bits which is not enough, meaning this character is at least 3 bytes.

10.. .... continuation of a multi-byte glyph

The last 6 bits of 0b11111011000 are 011000, therefore the next-last byte of the emoji is 10011000
```

```
new remaining = 0b11111............

There are 5 bits left to encode. A 'two or more' starting byte encodes 4 bits of data which is not enough, meaning this character is a total of 4 bytes.

10.. .... continuation of a multi-byte glyph

The last 6 bits of 0b11111 are 011111, therefore the next-last byte of the emoji is 10011111
```

```
new remaining = <none>

There are 0 bits left to encode.

The starting byte indicating three bytes follow is 1111 0...

The first byte of the emoji is 11110000.
```

> The final encoded character is `11110000 10011111 10011000 10101101`.

### Linked lists

Linked lists are a data structure that stores an ordered sequence of data nodes. Each node is made up of a piece of data, and a pointer to the location in memory of the next item in the linked list. The first node in the list is the "head" and the last node is the "tail".

The concept behind linked lists allows nodes to be inserted dynamically at any point within the list by creating a new node, and updating the point of the node before the location you wish to insert the data into.

```
Addr    Data    Next
0x00: | "abc" | 0x10 |
0x10: | "cde" | 0x20 |
0x20: | "efg" | 0x30 |
0x30: | "ghi" | NULL |
```

To add a new node between 0x10 and 0x20 with data `"xyz"`, it would look like this:

```
Addr    Data    Next
0x00: | "abc" | 0x10 |
0x10: | "cde" | 0x40 |
0x20: | "efg" | 0x30 |
0x30: | "ghi" | NULL |
0x40: | "xyz" | 0x20 |
```

If we follow this structure through, following pointers from the head to the tail (`NULL`), we get `"abc"` (`0x00`), `"cde"` (`0x10`), `"xyz"` (`0x40`), `"efg"` (`0x20`) and `"ghi"` (`0x30`).

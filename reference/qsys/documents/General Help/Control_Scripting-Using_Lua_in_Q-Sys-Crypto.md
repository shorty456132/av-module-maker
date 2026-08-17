# Crypto

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Crypto.htm

# Crypto

Use the Crypto commands to encode and decode ASCII text strings to and from Base64, as well as obtain CRC16, HMAC, and MD5 values for specified strings.

[Crypto.Base64Encode](javascript:void(0))

Compute the Base64 of a specified string.

### Syntax

Crypto.Base64Encode('*value*', [*pad*])

### Arguments

*value* : The value, enclosed within quotes, to encode to Base64.

*pad* : (Optional) Replace with **true** | **false**. If true, output is padded with '=' signs. The default is true.

### Examples

[Example 1: Encode with padding enabled](javascript:void(0))

```lua
print (Crypto.Base64Encode('Hello there'))
```

#### Debug Output

```lua
SGVsbG8gdGhlcmU=
```

[Example 2: Encode with padding disabled](javascript:void(0))

```lua
print (Crypto.Base64Encode('Hello there',false))
```

#### Debug Output

```lua
SGVsbG8gdGhlcmU
```

[Crypto.Base64Decode](javascript:void(0))

Convert the Base64 of a specified value to a string.

### Syntax

Crypto.Base64Decode('*value*')

### Arguments

*value* : The value, enclosed within quotes, to decode from Base64.

### Example

```lua
print (Crypto.Base64Decode('SGVsbG8gdGhlcmU='))
```

#### Debug Output

```lua
Hello there
```

[Crypto.CRC16Compute](javascript:void(0))

Compute the CRC16 of a specified value.

### Syntax

Crypto.CRC16Compute( '*value*' )

### Arguments

*value* : The value, enclosed within quotes, used to generate the CRC16.

### Example

```lua
Crypto.CRC16Compute('Hello there')
```

[Crypto.Cipher](javascript:void(0))

Table with values for supported ciphers.

### Syntax

Crypto.Cipher.*cipher*

### Arguments

*AES\_128\_CBC* : aes\_128\_cbc

*AES\_128\_ECB* : aes\_128\_ecb

*AES\_256\_CBC* : aes\_256\_cbc

*AES\_256\_ECB* : aes\_256\_ecb

**Note:** While there are many available ciphers in OpenSSL, these are specifically supported in Q-SYS.

### Example

```lua
Crypto.Cipher.AES_128_CBC
```

[Crypto.Decrypt](javascript:void(0))

Block-based decryption. Will raise error on failure.

### Syntax

Crypto.Decrypt ( *cipher*, *key*, *iv*, *cipher\_text* )

### Arguments

**Note:** `Crypto.Decrypt` requires that the `key` and `iv` match the length of the cipher

*cipher* : <string> - value from `Crypto.Ciphers` table

*key* : <string>

*iv* : <string> (can be empty)

*cipher\_text* : <string>

### Example

```lua
decrypted_iv = Crypto.Decrypt(Crypto.Cipher.AES_128_ECB,key,nil,encrypted_iv)
```

[Crypto.Digest](javascript:void(0))

Compute the message digest of specified data using a specified hashing algorithm.

### Syntax

Crypto.Digest('*algorithm*', '*data*')

### Arguments

*algorithm* : Replace with **md5** | **sha1** | **sha256** | **sha512** , enclosed within quotes.

*data* : The data for which to compute the message authentication code, enclosed within quotes.

### Example

```lua
Crypto.Digest('md5','Hello there')
```

[Crypto.Encrypt](javascript:void(0))

Block-based encryption. Will raise error on failure.

### Syntax

Crypto.Encrypt ( *cipher*, *key*, *iv*, *message*, *padding* )

### Arguments

**Note:** `Crypto.Encrypt` requires that the `key` and `iv` match the length of the cipher

*cipher* : <string> - value from `Crypto.Ciphers` table

*key* : <string>

*iv* : <string> (can be empty)

*message* : <string>

*padding* : <bool> default = true, if false then message must be multiple of block size

### Example

```lua
Crypto.Encrypt( Crypto.Cipher.AES_128_ECB, key, nil, iv, false )
```

[Crypto.GetRandomBytes](javascript:void(0))

Create a series of random bytes.

### Syntax

Crypto.GetRandomBytes(*count*)

### Arguments

*count* : <number>

### Example

```lua
Crypto.GetRandomBytes(13)
```

[Crypto.Hash](javascript:void(0))

Table with values for supported hash functions. Not all hashes are necessarily supported in every function.

### Syntax

Crypto.Hash.*hash\_function\_type*

### Arguments

*hash\_function\_type* : Replace with **MD5** | **SHA1** | **SHA256** | **SHA512**.

### Example

```lua
Crypto.Hash.MD5
```

[Crypto.HMAC](javascript:void(0))

Compute the message authentication code of specified data using a specified hashing algorithm and key.

### Syntax

Crypto.HMAC('*algorithm*', '*key*', '*data*')

### Arguments

*algorithm* : Replace with **md5** | **sha1** | **sha256** | **sha512** , enclosed within quotes.

*key* : The secret key to use for computing the message authentication code, enclosed within quotes.

*data* : The data for which to compute the message authentication code, enclosed within quotes.

### Example

```lua
Crypto.HMAC('md5','123456789','Hello there')
```

[Crypto.MD5Compute](javascript:void(0))

Compute the MD5 hash of a specified value.

### Syntax

Crypto.MD5Compute( '*value*' )

### Arguments

*value* : The value for which to compute the MD5 hash.

### Example

```lua
print (Crypto.MD5Compute('Hello there'))
```

#### Debug Output

```lua
e8ea7a8d1e93e8764a84a0f3df4644de
```

[Crypto.PBKDF2](javascript:void(0))

Implementation of Password-Based Key Derivation Function 2. Will raise error on failure.

### Syntax

Crypto.PBKDF2( '*value*' )

### Arguments

*password* : <string>

*salt* : <string>

*iterations* : <number>

*keylen* : <number>

*digest* : <string> - "*sha1*", "*sha256*", "*sha512*"

### Example

```lua
salt = string.char(0xaa, 0xef, 0x2d, 0x3f, 0x4d, 0x77, 0xac, 0x66, 0xe9, 0xc5, 0xa6, 0xc3, 0xd8, 0xf9, 0x21, 0xd1)  
password = "p@$Sw0rD~1"  
key = Crypto.PBKDF2(password, salt, 50000, 32, Crypto.Hash.SHA256)  
  
print(bitstring.hexdump(key))
```

#### Debug Output

```lua
2023-06-20T19:13:35.110	00000000: 52 c5 ef a1 6e 70 22 85   90 51 b1 de c2 8b c6 5d     R...np"..Q.....]
00000010: 96 96 a3 00 5d 0f 97 e5   06 c4 28 43 bc 3b db c0     ....].....(C.;..
```

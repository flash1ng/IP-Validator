from ipaddress import ip_address, IPv4Address


def validIPAddress(IP: str) -> str:
    """
    Validates if the input string is a valid IPv4 or IPv6 address.

    Args:
        IP (str): The IP address string to validate

    Returns:
        str: "IPv4" if valid IPv4, "IPv6" if valid IPv6, "Invalid" otherwise
    """
    try:
        # Try to create an IP address object from the string
        # If successful, check if it's IPv4 (otherwise it must be IPv6)
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        # The string is not a valid IP address format
        return "Invalid"


if __name__ == "__main__":
    # Test cases demonstrating different IP address scenarios

    # Case 1: Invalid IPv4 (too few octets)
    Ip = "192.168.5"
    print(validIPAddress(Ip))  # Expected: "Invalid"

    # Case 2: Valid IPv6 address
    Ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(validIPAddress(Ip))  # Expected: "IPv6"

    # Case 3: Invalid IPv4 (octet values out of range)
    Ip = "256.32.555.5"
    print(validIPAddress(Ip))  # Expected: "Invalid"

    # Case 4: Invalid format (mixed IPv4/IPv6 syntax)
    Ip = "250.32:555.5"
    print(validIPAddress(Ip))  # Expected: "Invalid"

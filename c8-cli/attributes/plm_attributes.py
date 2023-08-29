
"""_summary_

    Returns:
        _type_: _description_
"""
from plmprovider import C8Instance


def list_attributes(plm: C8Instance):
    """_summary_

    Args:
        plm (C8Instance): _description_

    Returns:
        _type_: _description_
    """
    # all_attributes = []
    plm.get_token()

    return ""


def count_attributes(plm: C8Instance):
    """_summary_

    Args:
        plm (C8Instance): _description_

    Returns:
        _type_: _description_
    """
    query = ('Module=Search&Operation=CountByXML&'
            'Qry.XML=<Query><Node Parameter="Type" '
            'Op="EQ" Value="CustomAttribute"/></Query>')
    response = plm.send_query(query)
    print(response)

    return ""


def main():
    """_summary_"""
    print("main")


if __name__ == "__main__":
    main()

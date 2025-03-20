import pandas as pd
from get_data import get_address
from func.utils import get_firstname, get_lastname


def main() -> None:
    data = get_address(50)
    data = pd.DataFrame(data)
    data["first_name"] = data.apply(
        lambda x: get_firstname(full_name=x["name"]),
        axis=1
    )
    data["last_name"] = data.apply(
        lambda x: get_lastname(full_name=x["name"]),
        axis=1
    )
    data: pd.DataFrame = data[
        [
            "first_name", 
            "last_name", 
            "house_number", 
            "street_name", 
            "city", 
            "post_code", 
            "country"
        ]
    ]
    print(data.head())


if __name__ == "__main__":
    main()
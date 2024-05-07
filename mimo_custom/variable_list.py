from pypika import Criterion, functions as fn

class NarrativeCriterions:
    @staticmethod
    def generate_criterion(function, column_name, criterion_type="", variable_list=None):
        """
        Generate a criterion based on the provided function, column name, and criterion type.

        Args:
            function (str): The function to apply to the column. Currently supports "Upper".
            column_name (str): The name of the column to apply the function to.
            criterion_type (str, optional): The type of criterion to generate. Valid options are "all", "any", and "IN".
            variable_list (list, optional): A list of variables to use in the criterion.

        Returns:
            Criterion: The generated criterion.

        Raises:
            ValueError: If an invalid function or criterion type is provided.
        """
        try:
            if function == "Upper":
                if criterion_type == "any":
                    return Criterion.any([fn.Upper(column_name).like(variable) for variable in variable_list])
                elif criterion_type == "all":
                    return Criterion.all([fn.Upper(column_name).like(variable) for variable in variable_list])
                else:
                    raise ValueError("Invalid criterion type.") 
            elif function == "" and criterion_type == "IN":
                return getattr(column_name, "isin")(variable_list)
            else:
                raise ValueError("Invalid function or criterion type.")
        except ValueError as e:
            print(f"Error occurred: {e}")
            raise e

# Usage example:
result_criterion = NarrativeCriterions.generate_criterion("Upper", "column_name", "any", ["var1", "var2"])

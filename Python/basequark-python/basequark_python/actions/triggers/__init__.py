"""
controller to consume various inputs by user or lifecycle events
> NOTE: this directory should handle _all_ user inputs. It has no limit on where the results of the input can be dispatched.
>
> - most likely it will be to one of the `/processes` files
>
> But **no** other directory should interact with a user action.
"""

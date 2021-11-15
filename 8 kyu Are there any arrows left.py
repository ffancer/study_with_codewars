def any_arrows(arrows):
    return any(not i.get("damaged", False) for i in arrows)


print(any_arrows([]), False, "Should handle empty quiver")
print(any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]), True,
      "Should handle quiver with undamaged arrows")
print(any_arrows([{'range': 10, 'damaged': True}, {'damaged': True}]), False,
      "Should handle quiver with damaged arrows")

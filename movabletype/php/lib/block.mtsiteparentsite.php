<?php
# Movable Type (r) (C) 2001-2017 Six Apart, Ltd. All Rights Reserved.
# This code cannot be redistributed without permission from www.sixapart.com.
# For more information, consult your Movable Type license.
#
# $Id$
function smarty_block_mtsiteparentsite($args, $content, &$ctx, &$repeat) {
    return smarty_block_mtblogparentwebsite($args, $content, $ctx, $repeat);
}
?>
